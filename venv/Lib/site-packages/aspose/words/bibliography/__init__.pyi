import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class Bibliography:
    """Represents the list of bibliography sources available in the document."""
    
    @property
    def bibliography_style(self) -> str:
        """Gets a string that represents the name of the active style to use for a bibliography."""
        ...
    
    @property
    def sources(self) -> List[aspose.words.bibliography.Source]:
        """Gets a collection that represents all the sources contained in a bibliography."""
        ...
    
    ...

class Contributor:
    """Represents a bibliography source contributor. Can be either an corporate (an organization) or a list of persons."""
    
    def as_person_collection(self) -> aspose.words.bibliography.PersonCollection:
        """Casts contributor to :class:`PersonCollection`, otherwise returns null."""
        ...
    
    def as_corporate(self) -> aspose.words.bibliography.Corporate:
        """Casts contributor to :class:`Corporate`, otherwise returns null."""
        ...
    
    ...

class ContributorCollection:
    """Represents bibliography source contributors."""
    
    @property
    def artist(self) -> aspose.words.bibliography.Contributor:
        """Gets the artist of a source."""
        ...
    
    @property
    def author(self) -> aspose.words.bibliography.Contributor:
        """Gets the author of a source."""
        ...
    
    @property
    def book_author(self) -> aspose.words.bibliography.Contributor:
        """Gets the book author of a source."""
        ...
    
    @property
    def compiler(self) -> aspose.words.bibliography.Contributor:
        """Gets the compiler of a source."""
        ...
    
    @property
    def composer(self) -> aspose.words.bibliography.Contributor:
        """Gets the composer of a source."""
        ...
    
    @property
    def conductor(self) -> aspose.words.bibliography.Contributor:
        """Gets the conductor of a source."""
        ...
    
    @property
    def counsel(self) -> aspose.words.bibliography.Contributor:
        """Gets the counsel of a source."""
        ...
    
    @property
    def director(self) -> aspose.words.bibliography.Contributor:
        """Gets the director of a source."""
        ...
    
    @property
    def editor(self) -> aspose.words.bibliography.Contributor:
        """Gets the editor of a source."""
        ...
    
    @property
    def interviewee(self) -> aspose.words.bibliography.Contributor:
        """Gets the interviewee of a source."""
        ...
    
    @property
    def interviewer(self) -> aspose.words.bibliography.Contributor:
        """Gets the interviewer of a source."""
        ...
    
    @property
    def inventor(self) -> aspose.words.bibliography.Contributor:
        """Gets the inventor of a source."""
        ...
    
    @property
    def performer(self) -> aspose.words.bibliography.Contributor:
        """Gets the performer of a source."""
        ...
    
    @property
    def producer(self) -> aspose.words.bibliography.Contributor:
        """Gets the producer of a source."""
        ...
    
    @property
    def translator(self) -> aspose.words.bibliography.Contributor:
        """Gets the translator of a source."""
        ...
    
    @property
    def writer(self) -> aspose.words.bibliography.Contributor:
        """Gets the writer of a source."""
        ...
    
    ...

class Corporate(aspose.words.bibliography.Contributor):
    """Represents a corporate (an organization) bibliography source contributor."""
    
    @property
    def name(self) -> str:
        """Gets the name of a organization."""
        ...
    
    ...

class Person:
    """Represents individual (a person) bibliography source contributor."""
    
    @property
    def last(self) -> str:
        """Gets the last name of a person."""
        ...
    
    @property
    def first(self) -> str:
        """Gets the first name of a person."""
        ...
    
    @property
    def middle(self) -> str:
        """Gets the middle name of a person."""
        ...
    
    ...

class PersonCollection(aspose.words.bibliography.Contributor):
    """Represents a list of persons who are bibliography source contributors."""
    
    def __getitem__(self, index: int) -> aspose.words.bibliography.Person:
        """Returns a person at the specified index.
        
        :param index: An index into the collection."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of elements contained in the collection."""
        ...
    
    ...

class Source:
    """Represents an individual source, such as a book, journal article, or interview."""
    
    @property
    def lcid(self) -> str:
        """Gets the locale ID of a source."""
        ...
    
    @property
    def contributors(self) -> aspose.words.bibliography.ContributorCollection:
        """Gets contributors list (author, editor, writer etc) of a source."""
        ...
    
    @property
    def source_type(self) -> aspose.words.bibliography.SourceType:
        """Gets the source type of a source."""
        ...
    
    @property
    def abbreviated_case_number(self) -> str:
        """Gets the abbreviated case number of a source."""
        ...
    
    @property
    def album_title(self) -> str:
        """Gets the album title of a source."""
        ...
    
    @property
    def book_title(self) -> str:
        """Gets the book title of a source."""
        ...
    
    @property
    def broadcaster(self) -> str:
        """Gets the broadcaster of a source."""
        ...
    
    @property
    def broadcast_title(self) -> str:
        """Gets the broadcast title of a source."""
        ...
    
    @property
    def case_number(self) -> str:
        """Gets the case number of a source."""
        ...
    
    @property
    def chapter_number(self) -> str:
        """Gets the chapter number of a source."""
        ...
    
    @property
    def city(self) -> str:
        """Gets the city of a source."""
        ...
    
    @property
    def comments(self) -> str:
        """Gets the comments of a source."""
        ...
    
    @property
    def conference_name(self) -> str:
        """Gets the conference or proceedings name of a source."""
        ...
    
    @property
    def country_or_region(self) -> str:
        """Gets the country or region of a source."""
        ...
    
    @property
    def court(self) -> str:
        """Gets the court of a source."""
        ...
    
    @property
    def day(self) -> str:
        """Gets the day of a source."""
        ...
    
    @property
    def day_accessed(self) -> str:
        """Gets the day accessed of a source."""
        ...
    
    @property
    def department(self) -> str:
        """Gets the department of a source."""
        ...
    
    @property
    def distributor(self) -> str:
        """Gets the distributor of a source."""
        ...
    
    @property
    def edition(self) -> str:
        """Gets the editor of a source."""
        ...
    
    @property
    def guid(self) -> str:
        """Gets the guid of a source."""
        ...
    
    @property
    def institution(self) -> str:
        """Gets the institution of a source."""
        ...
    
    @property
    def internet_site_title(self) -> str:
        """Gets the internet site title of a source."""
        ...
    
    @property
    def issue(self) -> str:
        """Gets the issue of a source."""
        ...
    
    @property
    def journal_name(self) -> str:
        """Gets the journal name of a source."""
        ...
    
    @property
    def medium(self) -> str:
        """Gets the medium of a source."""
        ...
    
    @property
    def month(self) -> str:
        """Gets the month of a source."""
        ...
    
    @property
    def month_accessed(self) -> str:
        """Gets the month accessed of a source."""
        ...
    
    @property
    def number_volumes(self) -> str:
        """Gets the number of volumes of a source."""
        ...
    
    @property
    def pages(self) -> str:
        """Gets the pages of a source."""
        ...
    
    @property
    def patent_number(self) -> str:
        """Gets the patent number of a source."""
        ...
    
    @property
    def periodical_title(self) -> str:
        """Gets the periodical title of a source."""
        ...
    
    @property
    def production_company(self) -> str:
        """Gets the production company of a source."""
        ...
    
    @property
    def publication_title(self) -> str:
        """Gets the publication title of a source."""
        ...
    
    @property
    def publisher(self) -> str:
        """Gets the publisher of a source."""
        ...
    
    @property
    def recording_number(self) -> str:
        """Gets the recording number of a source."""
        ...
    
    @property
    def ref_order(self) -> str:
        """Gets the reference order of a source."""
        ...
    
    @property
    def reporter(self) -> str:
        """Gets the reporter of a source."""
        ...
    
    @property
    def short_title(self) -> str:
        """Gets the short title of a source."""
        ...
    
    @property
    def standard_number(self) -> str:
        """Gets the standard number of a source."""
        ...
    
    @property
    def state_or_province(self) -> str:
        """Gets the state or province of a source."""
        ...
    
    @property
    def station(self) -> str:
        """Gets the station of a source."""
        ...
    
    @property
    def tag(self) -> str:
        """Gets the identifying tag name of a source."""
        ...
    
    @property
    def theater(self) -> str:
        """Gets the theater of a source."""
        ...
    
    @property
    def thesis_type(self) -> str:
        """Gets the thesis type of a source."""
        ...
    
    @property
    def title(self) -> str:
        """Gets the title of a source."""
        ...
    
    @property
    def type(self) -> str:
        """Gets the type of a source."""
        ...
    
    @property
    def url(self) -> str:
        """Gets the url of a source."""
        ...
    
    @property
    def version(self) -> str:
        """Gets the version of a source."""
        ...
    
    @property
    def volume(self) -> str:
        """Gets the volume of a source."""
        ...
    
    @property
    def year(self) -> str:
        """Gets the year of a source."""
        ...
    
    @property
    def year_accessed(self) -> str:
        """Gets the year accessed of a source."""
        ...
    
    ...

class SourceType(Enum):
    """Represents bibliography source types."""
    
    """Specifies the article in a periodical source."""
    ARTICLE_IN_A_PERIODICAL: int
    
    """Specifies the book source."""
    BOOK: int
    
    """Specifies the book section source."""
    BOOK_SECTION: int
    
    """Specifies the journal article source."""
    JOURNAL_ARTICLE: int
    
    """Specifies the conference proceedings source."""
    CONFERENCE_PROCEEDINGS: int
    
    """Specifies the reporter source."""
    REPORT: int
    
    """Specifies the sound recording source."""
    SOUND_RECORDING: int
    
    """Specifies the performance source."""
    PERFORMANCE: int
    
    """Specifies the art source."""
    ART: int
    
    """Specifies the document from internet site source."""
    DOCUMENT_FROM_INTERNET_SITE: int
    
    """Specifies the internet site source."""
    INTERNET_SITE: int
    
    """Specifies the film source."""
    FILM: int
    
    """Specifies the interview source."""
    INTERVIEW: int
    
    """Specifies the patent source."""
    PATENT: int
    
    """Specifies the electronic source."""
    ELECTRONIC: int
    
    """Specifies the case source."""
    CASE: int
    
    """Specifies the miscellaneous source."""
    MISC: int
    

